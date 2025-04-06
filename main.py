import pygame
import neat
import time
import os
import random 

WIN_WIDTH=600
WIN_HEIGHT=800



BIRD_IMGS=[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png")))]
PIPE_IMG=pygame.transform.scale2x(pygame.image.load(os.load.join("imgs","pipe.png")))
BASE_IMG=pygame.transform.scale2x(pygame.image.load(os.load.join("imgs","base.png")))
BG_IMG=pygame.transform.scale2x(pygame.image.load(os.load.join("imgs","bg.png")))