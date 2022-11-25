from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.mixins import AuditMixin
from apps.common.oneTextField import OneTextField
from apps.common.fileUpload.userPath import userDirectoryPath


class Card(AuditMixin):
    user = models.ForeignKey(User, related_name='products_type', blank=True, on_delete=models.CASCADE,
                             null=True, verbose_name=_('Kullanıcı'))
    number = models.CharField(max_length=200, null=True, verbose_name=_('Kart Numarası'))
    name = models.CharField(max_length=200, null=True, verbose_name=_('Kart Sahibi'))
    expiry = models.CharField(max_length=200, null=True, verbose_name=_('Son Kullanım Tarihi'))
    cvc = models.CharField(max_length=200, null=True, verbose_name=_('CVC'))

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('Kartlar')
        verbose_name_plural = _('Kartlar')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
