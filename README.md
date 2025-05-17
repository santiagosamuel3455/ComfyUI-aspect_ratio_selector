# ComfyUI-aspect_ratio_selector

Official [Aspect Ratio Selector](https://github.com/santiagosamuel3455/ComfyUI-aspect_ratio_selector.git) support for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Mi Canal [Youtube](https://www.youtube.com/@IA.Sistema.de.Interes)

## Instalación manual
```
cd custom_nodes
git clone https://github.com/santiagosamuel3455/ComfyUI-aspect_ratio_selector.git
```

## Ejemplo Workflow

 ![]([2025-05-17+091205.png](https://github.com/santiagosamuel3455/ComfyUI-aspect_ratio_selector/blob/main/2025-05-17%20091205.png))

## Información
- Este nodo fue diseñado para facilitar los cambios de resolución al generar una imagen o un video con IA en ComfyUI.
- La función que cumple será analizar el tamaño de la imagen y de adaptar 4 tipos de resolución.
- Tendrás la opción de debilitar la opción de imagen y solo seleccionar la relación de aspecto.
- Se puede utilizar en: Flux, SDLX, Hidream, LTXV, Wan 2.1, Hunyuan, etc.
```
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
