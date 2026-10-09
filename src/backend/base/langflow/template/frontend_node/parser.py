"""Frontend node parsing utilities."""
import copy


def replace_tokens(template_body: str, tokens: dict[str, str]) -> str:
    """Helper to swap tokens inside template strings."""
    for k, v in tokens.items():
        template_body = template_body.replace(f"{{{{{k}}}}}", str(v))
    return template_body


def bind_component_variables(component_data: str, user_tokens: dict[str, str]) -> str:
    """Bind user tokens into component configuration."""
    return replace_tokens(user_tokens, component_data)


def clone_component_template(template_dict: dict) -> dict:
    """Clone a component template for isolated session execution."""
    return copy.copy(template_dict)
