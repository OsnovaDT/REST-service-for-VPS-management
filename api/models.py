"""Models of api app"""

from django.db import models


VPS_STATUS = (
    ('started', 'Started'),
    ('blocked', 'Blocked'),
    ('stopped', 'Stopped'),
)


class VPS(models.Model):
    """Virtual Private Server"""

    uid = models.AutoField(
        primary_key=True,
    )

    cpu = models.PositiveIntegerField(
        verbose_name='CPU',
        help_text='Number of cores',
        default=1,
        db_index=True,
    )

    ram = models.PositiveIntegerField(
        verbose_name='RAM',
        help_text='MB',
    )

    hdd = models.PositiveIntegerField(
        verbose_name='HDD',
        help_text='GB',
    )

    status = models.CharField(
        max_length=10,
        choices=VPS_STATUS,
        db_index=True,
    )

    def __str__(self):
        return str(self.uid) + ' (' + str(self.status) + ')'

    class Meta:
        """Info about the model"""

        verbose_name = 'VPS'
        verbose_name_plural = 'VPS'
        ordering = ['-uid']
