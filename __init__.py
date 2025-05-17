# __init__.py

from .aspect_ratio_selector_node import AspectRatioSelectorNode

NODE_CLASS_MAPPINGS = {
    "AspectRatioSelectorNode": AspectRatioSelectorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioSelectorNode": "Aspect Ratio Selector Node"
}

#WEB_DIRECTORY = "./web"  # opcional, si usas UI adicional
__version__ = "1.2.0"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
