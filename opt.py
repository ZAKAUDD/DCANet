import argparse
import os


parse = argparse.ArgumentParser(description='PyTorch Polyp Segmentation')

"-------------------data option--------------------------"
parse.add_argument('--root', type=str, default='/media/zaka/92A816A5A81687BD/PaperCoding/Ablationstudy/ACSNet-master/')
parse.add_argument('--dataset', type=str, default='kvasir_SEG') #KavSir-SEG,, EndoScene
parse.add_argument('--train_data_dir', type=str, default='DataSet/train')
parse.add_argument('--valid_data_dir', type=str, default='DataSet/valid')
#parse.add_argument('--test_data_dir', type=str, default='DataSet/testdata/CVC-ColonDB') #DataSet/testdata/ETIS-LaribPolypDB
#parse.add_argument('--test_data_dir', type=str, default='DataSet/testdata/CVC-300')
#parse.add_argument('--test_data_dir', type=str, default='DataSet/testdata/CVC-ClinicDB')
#parse.add_argument('--test_data_dir', type=str, default='DataSet/testdata/ETIS-LaribPolypDB')
parse.add_argument('--test_data_dir', type=str, default='DataSet/testdata/Kvasir')


"-------------------training option-----------------------"
parse.add_argument('--mode', type=str, default='test')
parse.add_argument('--nEpoch', type=int, default=150)
parse.add_argument('--batch_size', type=float, default=4)
parse.add_argument('--num_workers', type=int, default=2)
parse.add_argument('--use_gpu', type=bool, default=True)
parse.add_argument('--load_ckpt', type=str, default='ck_150')
parse.add_argument('--model', type=str, default='ACSNet')
parse.add_argument('--expID', type=int, default=3)
parse.add_argument('--ckpt_period', type=int, default=5)

"-------------------optimizer option-----------------------"
parse.add_argument('--lr', type=float, default=1e-3)
parse.add_argument('--weight_decay', type=float, default=1e-5)
parse.add_argument('--mt', type=float, default=0.9)
parse.add_argument('--power', type=float, default=0.9)

parse.add_argument('--nclasses', type=int, default=1)

opt = parse.parse_args()
