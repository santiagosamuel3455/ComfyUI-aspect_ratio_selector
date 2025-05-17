# ComfyUI-aspect_ratio_selector

Official [Aspect Ratio Selector](https://github.com/santiagosamuel3455/ComfyUI-aspect_ratio_selector.git) support for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Mi Canal [Youtube](https://www.youtube.com/@IA.Sistema.de.Interes)

## Instalacion manual
```
cd custom_nodes
git clone https://github.com/santiagosamuel3455/ComfyUI-aspect_ratio_selector.git
```

## Ejemplo Workflow

 ![](2025-05-17+091205.png)

## Informacion
- Este nodo fue diseñado para facilitar los cambioos de resolucion al generar una imagen o un video con IA en ComfyUI.
- La funcion que cumple sera analizar el tamaño de la imageen y de adaptar 4 tipo de resolucioins.
- Tendras la opcion de deabilitar la opcioin de imagen y solo selecioanr la relacion de aspecto.
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
