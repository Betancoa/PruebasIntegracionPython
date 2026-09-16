class DiscountEngine:
    # Regla: >=100 → 10%, >=50 → 5%, >=200 → 15%, otro → 0%
    def discount_for(self, subtotal: float) -> float:
        if subtotal >= 100.0:
            return 0.10
        if subtotal >= 50.0:
            return 0.05
        if subtotal >=200.0:
            return 0.15
        return 0.0