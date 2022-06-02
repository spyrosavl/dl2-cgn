from yacs.config import CfgNode as CN

__C = CN()

cfg = __C

# General
__C.MODEL_NAME = 'tmp'
__C.BlGAN_WEIGHTS_PATH = "/home/lcur1339/dl2-cgn/cgn_framework/imagenet/weights/blend_net_weights"
__C.CGN_WEIGHTS_PATH = "/home/lcur1339/dl2-cgn/cgn_framework/imagenet/weights/cgn.pth"
__C.DISC_WEIGHTS_PATH = ''

# Logging
__C.LOG = CN()
__C.LOG.SAVE_ITER = 1
__C.LOG.SAMPLED_FIXED_NOISE = False
__C.LOG.SAVE_SINGLES = False
__C.LOG.LOSSES = True

# Model
__C.MODEL = CN()
__C.MODEL.RES = 256
__C.MODEL.TRUNCATION = 1.0

# Training
__C.TRAIN = CN()
__C.TRAIN.EPOCHS = 50
__C.TRAIN.BATCH_SZ = 256
__C.TRAIN.BATCH_ACC = 8

# Loss Weigths
__C.LAMBDA = CN()
__C.LAMBDA.L2 = 0.99
__C.LAMBDA.ADV = 0.01


# Learning Rates
__C.LR = CN()
__C.LR.BGAN = 2e-3
__C.LR.DISC = 3e-4

def get_cfg_gp_gan_defaults():
    return __C.clone()
