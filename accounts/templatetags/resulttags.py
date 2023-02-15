from django import template

register = template.Library()


@register.filter(is_safe=True)    
# is_safe argument tells django that the underlying function will not return any characters that could break HTML
def get_result(result:dict, subject: str) -> int:
    """Returns the marks obtained from the result dictionary based on the passed subject

    Args:
        result (dict): Dictionary containing the results
        subject (str): Subject to obtain the marks of

    Returns:
        int: marks obtained
    """
    marks = result[subject]

    return marks