from __future__ import unicode_literals
import pkgutil
import re

import django.core.mail
from django.conf import settings
from django.template.loader import render_to_string
from mailer import send_html_mail
import mailer.models
import html2text

from pyweek.users.models import EmailAddress


# Extend the django-mailer priorities with PRIORITY_IMMEDIATE
# that allows skipping the queue. This is mostly important
# for e-mail validation, which is effectively an interactive
# process.
PRIORITY_LOW = mailer.models.PRIORITY_LOW
PRIORITY_MEDIUM = mailer.models.PRIORITY_MEDIUM
PRIORITY_HIGH = mailer.models.PRIORITY_HIGH
PRIORITY_IMMEDIATE = float('inf')


REASON_COMMENTS = (
    "because you are set to receive replies to diary and discussion posts."
)


class InvalidTemplate(Exception):
    """The selected template does not exist."""


def _make_payload(body_html, reason):
    converter = html2text.HTML2Text()
    converter.inline_links = False
    body_text = converter.handle(body_html).strip()
    ctx = {
        'body_html': body_html,
        'body_text': body_text,
        'reason': reason,
    }
    html_part = render_to_string('mail/admin_email.html', context=ctx)
    text_part = render_to_string('mail/admin_email.txt', context=ctx)
    return html_part, text_part


WS_RE = re.compile(r'[\r\n]+')


def clean_header(v):
    """Clean a header value, removing illegal characters."""
    return WS_RE.sub(' ', v)


def send(
        subject,
        html_body,
        recipients,
        reason,
        priority=mailer.models.PRIORITY_MEDIUM):
    """Send an e-mail, using the django-mailer queue."""
    html_part, text_part = _make_payload(html_body, reason)
    subject = '[PyWeek] {}'.format(subject.strip())

    #TODO: identify sending user rather than using default
    from_email = settings.DEFAULT_FROM_EMAIL
    for recip in recipients:
        if isinstance(recip, EmailAddress):
            to_email = '{} <{}>'.format(recip.user.username, recip.address)
        else:
            to_email = recip

        to_email = clean_header(to_email)
        subject = clean_header(subject.strip())

        if priority == PRIORITY_IMMEDIATE:
            django.core.mail.send_mail(
                subject=subject,
                message=text_part,
                html_message=html_part,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                fail_silently=False,
            )
        else:
            send_html_mail(
                subject=subject,
                message=text_part,
                message_html=html_part,
                from_email=from_email,
                recipient_list=[to_email],
                priority=priority,
            )


def send_template(
        subject,
        template_name,
        recipients,
        params,
        reason,
        priority=mailer.models.PRIORITY_MEDIUM):
    """Send a queued message from a template."""
    html_body = render_to_string(
        'emails/{}.html'.format(template_name),
        context=params
    )
    return send(
        subject,
        html_body,
        recipients,
        reason,
        priority=priority
    )
