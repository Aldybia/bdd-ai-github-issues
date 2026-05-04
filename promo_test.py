def promo_price(total, payment):
    if total >= 500_000 and payment.lower() == "shopeepay":
        return total * 0.9
    return total

# Test Case 1: Positif - belanja >= 500000 dengan ShopeePay
assert promo_price(500_000, "ShopeePay") == 450_000, "TC1 FAILED"

# Test Case 2: Negatif - belanja < 500000
assert promo_price(499_999, "ShopeePay") == 499_999, "TC2 FAILED"

# Test Case 3: Negatif - pembayaran bukan ShopeePay
assert promo_price(550_000, "OVO") == 550_000, "TC3 FAILED"

print("Semua test case PASSED!")
