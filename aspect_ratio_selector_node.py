# aspect_ratio_selector_node.py

class AspectRatioSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "quality": (["MIN SD", "SD", "HD", "Full HD"], {"default": "SD", "refreshable": True}),
                "aspect_ratio": (cls.get_aspect_ratios("SD"), {"default": "16:9", "refreshable": True})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"
    CATEGORY = "Custom Nodes/Input"

    # Definición de resoluciones según calidad y aspect ratio
    resolutions = {
        "MIN SD": {
            "16:9": [(640, 360)],
            "1:1": [(480, 480)],
            "9:16": [(360, 640)]
        },
        "SD": {
            "16:9": [(854, 480)],
            "1:1": [(480, 480)],
            "9:16": [(480, 854)]
        },
        "HD": {
            "16:9": [(1280, 720)],
            "1:1": [(720, 720)],
            "9:16": [(720, 1280)]
        },
        "Full HD": {
            "16:9": [(1920, 1080)],
            "1:1": [(1080, 1080)],
            "9:16": [(1080, 1920)]
        }
    }

    @classmethod
    def get_aspect_ratios(cls, quality):
        return list(cls.resolutions[quality].keys())

    @classmethod
    def REFRESH_INPUTS(cls, input_types):
        # Actualiza las opciones de 'aspect_ratio' cuando cambia 'quality'
        if "quality" in input_types["required"]:
            selected_quality = input_types["required"]["quality"][0][0]
            new_aspect_ratios = cls.get_aspect_ratios(selected_quality)
            input_types["required"]["aspect_ratio"] = (new_aspect_ratios,)
        return input_types

    def get_size(self, quality, aspect_ratio):
        # Selecciona la primera resolución disponible para esa combinación
        width, height = self.resolutions[quality][aspect_ratio][0]
        return (width, height)