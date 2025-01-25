
import torch
from catt.ed_pl import TashkeelModel
from catt.tashkeel_tokenizer import TashkeelTokenizer
from catt.utils import remove_non_arabic

tokenizer = TashkeelTokenizer()
ckpt_path = 'models/best_ed_mlm_ns_epoch_178.pt'

print('ckpt_path is:', ckpt_path)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('device:', device)

max_seq_len = 1024
print('Creating Model...')
model = TashkeelModel(tokenizer, max_seq_len=max_seq_len, n_layers=3, learnable_pos_emb=False)

model.load_state_dict(torch.load(ckpt_path, map_location=device))
model.eval().to(device)

# list of undiacritized texts
x = ['وقالت مجلة نيوزويك الأمريكية التحديث الجديد ل إنستجرام يمكن أن يساهم في إيقاف وكشف الحسابات المزورة بسهولة شديدة']

x = [remove_non_arabic(i) for i in x]
batch_size = 16
verbose = True
x_tashkeel = model.do_tashkeel_batch(x, batch_size, verbose)

print(x)
print('-'*85)
print(x_tashkeel)
