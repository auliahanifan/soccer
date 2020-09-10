def conditional_decorator(condition, decorator):
    return decorator if condition else lambda x: x
