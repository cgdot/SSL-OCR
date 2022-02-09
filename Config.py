baseDir_word = '/home/mohamed/vit/SSL-OCR/data/icdar13/'
baseDir_line = '/home/mohamed/vit/SSL-OCR/data/icdar13/'


#OUTPUT_MAX_LEN = 95  ## iam lines 
OUTPUT_MAX_LEN = 38  ## iam words

#baseDir_word = '/data2fast/users/msouibgui/maedata/syntdata/'
#baseDir_line = '/data2fast/users/msouibgui/maedata/syntdata/'
#OUTPUT_MAX_LEN  = 180 ##synthetic

TRAINTYPE = 'IAM-scratch'
SETTING = 'base'
DATATYPE = 'word'
continue_train = False
batch_size = 12


patch_size = 8
image_size =  (128,512)
MASKINGRATIO = 0.75
VIS_RESULTS = True

if SETTING == 'base':
    NUM_ENCODER_LAYERS = 6
    NUM_DECODER_LAYERS = 6
    EMB_SIZE = 768
    NHEAD = 8
    FFN_HID_DIM = 768

if SETTING == 'small':
    NUM_ENCODER_LAYERS = 3
    NUM_DECODER_LAYERS = 3
    EMB_SIZE = 512
    NHEAD = 4
    FFN_HID_DIM = 512
