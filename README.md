# latex_2_math_util

Docker util based on:

```bibtex
@MISC {4578197,
    TITLE = {Convert latex to wolframalpha.com compatible expression},
    AUTHOR = {Sam (https://math.stackexchange.com/users/1107492/sam)},
    HOWPUBLISHED = {Mathematics Stack Exchange},
    NOTE = {URL:https://math.stackexchange.com/q/4578197 (version: 2022-11-16)},
    EPRINT = {https://math.stackexchange.com/q/4578197},
    URL = {https://math.stackexchange.com/q/4578197}
}
```

## Setup

```bash
cd .docker \
docker compose build
```


## Run

```bash
cd .docker \
docker compose run --rm "\text{Your latex expression here}" \
# Ex:
docker compose run --rm latex2math "\int_{0}^{1}\left(3\left(\frac{3 e^{-4 + 2t}}{3 e^{-4} + 1} + \frac{e^{-2t}}{3e^{-4} + 1}\right)^2 + \left(\frac{3 e^{-4 + 2t}}{3 e^{-4} + 1} - \frac{3 e^{-2t}}{3e^{-4} + 1}\right)^2 \right) dt"
```