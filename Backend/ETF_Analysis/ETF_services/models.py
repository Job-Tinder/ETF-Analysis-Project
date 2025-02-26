from django.db import models

# Create your models here.


class ETF_holdings(models.Model):
    ticker = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    asset_class = models.CharField(max_length=100)
    market_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    notional_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    shares = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    exchange = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    fx_rate = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    market_currency = models.CharField(max_length=10, null=True, blank=True)
    accrual_date = models.DateField(null=True, blank=True)
    etfname = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(blank=True,null=True)
    firm=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.ticker} - {self.date}'
    
    class Meta:
        db_table="ETF_holdings"

class Stock(models.Model):
    stock_name=models.CharField(max_length=100)
    stock_shortname=models.CharField(max_length=100)
    
    class Meta:
         db_table="Stock"
class ETF(models.Model):
    etf_name=models.CharField(max_length=100)
    etf_shortname=models.CharField(max_length=30)
    etf_link=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    stocks=models.ManyToManyField(to=Stock)
    
    class Meta:
         db_table="ETF"

class AvailabilityDate(models.Model):
    date=models.DateField(blank=True,null=True)
    is_available=models.BooleanField(default=False)
    
    class Meta:
        db_table="AvailabilityDate"
    

    
