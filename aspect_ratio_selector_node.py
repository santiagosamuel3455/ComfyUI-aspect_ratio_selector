# aspect_ratio_selector_node.py

class AspectRatioSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "quality": (["MIN SD", "SD", "HD", "Full HD"], {"default": "SD", "refreshable": True}),
                "aspect_ratio": (cls.get_aspect_ratios("SD"), {"default": "16:9", "refreshable": True}),
                "analyze_image": (["enable", "disable"], {"default": "enable"})
            },
            "optional": {
                "image": ("IMAGE",)
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"
    CATEGORY = "Custom Nodes/Input"

    # Máximo tamaño permitido por calidad (cuadrado máximo)
    max_dimensions = {
        "MIN SD": 640,
        "SD": 854,
        "HD": 1280,
        "Full HD": 1920
    }

    # Resoluciones fijas por ratio y calidad (para modo manual)
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
        if "quality" in input_types["required"]:
            selected_quality = input_types["required"]["quality"][0][0]
            new_aspect_ratios = cls.get_aspect_ratios(selected_quality)
            input_types["required"]["aspect_ratio"] = (new_aspect_ratios,)
        return input_types

    def get_size(self, quality, aspect_ratio, analyze_image, image=None):
        if analyze_image == "enable" and image is not None:
            # Obtener dimensiones originales de la imagen
            _, height, width, _ = image.shape  # Formato de imagen en ComfyUI: [batch, H, W, channels]
            aspect = width / height

            # Obtener el tamaño máximo permitido por la calidad
            max_size = self.max_dimensions[quality]

            # Calcular nuevas dimensiones manteniendo el aspecto
            if aspect > 1:  # Landscape (ancho > alto)
                new_width = int(max_size)
                new_height = int(max_size / aspect)
            else:  # Portrait o cuadrado (alto >= ancho)
                new_height = int(max_size)
                new_width = int(max_size * aspect)

            return (new_width, new_height)
        else:
            # Usar resolución fija según aspect_ratio y calidad
            width, height = self.resolutions[quality][aspect_ratio][0]
            return (width, height)
