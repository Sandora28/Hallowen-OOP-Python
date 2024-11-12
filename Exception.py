

class InsufficientStockError(Exception):
    """Raised when there is not enough stock for a requested costume."""
    pass

class InsufficientBudgetError(Exception):
    """Raised when the customer does not have enough budget for the purchase."""
    pass

class CostumeNotFoundError(Exception):
    """Raised when the requested costume cannot be found in any shop."""
    pass