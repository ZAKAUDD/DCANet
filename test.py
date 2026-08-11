# import torch
# from tqdm import tqdm
# from opt import opt
# from utils.metrics import evaluate
# import datasets
# from torch.utils.data import DataLoader
# from utils.comm import generate_model
# from utils.metrics import Metrics


# def test():
#     print('loading data......')
#     test_data = getattr(datasets, opt.dataset)(opt.root, opt.test_data_dir, mode='test')
#     test_dataloader = DataLoader(test_data, batch_size=1, shuffle=False, num_workers=opt.num_workers)
#     total_batch = int(len(test_data) / 1)
#     model = generate_model(opt)

#     model.eval()

#     # metrics_logger initialization
#     metrics = Metrics(['recall', 'specificity', 'precision', 'F1', 'F2',
#                        'ACC_overall', 'IoU_poly', 'IoU_bg', 'IoU_mean'])

#     with torch.no_grad():
#         bar = tqdm(enumerate(test_dataloader), total=total_batch)
#         for i, data in bar:
#             img, gt = data['image'], data['label']

#             if opt.use_gpu:
#                 img = img.cuda()
#                 gt = gt.cuda()

#             output = model(img)
#             _recall, _specificity, _precision, _F1, _F2, \
#             _ACC_overall, _IoU_poly, _IoU_bg, _IoU_mean = evaluate(output, gt)

#             metrics.update(recall= _recall, specificity= _specificity, precision= _precision, 
#                             F1= _F1, F2= _F2, ACC_overall= _ACC_overall, IoU_poly= _IoU_poly, 
#                             IoU_bg= _IoU_bg, IoU_mean= _IoU_mean
#                         )

#     metrics_result = metrics.mean(total_batch)

#     print("Test Result:")
#     print('recall: %.4f, specificity: %.4f, precision: %.4f, F1: %.4f, F2: %.4f, '
#           'ACC_overall: %.4f, IoU_poly: %.4f, IoU_bg: %.4f, IoU_mean: %.4f'
#           % (metrics_result['recall'], metrics_result['specificity'], metrics_result['precision'],
#              metrics_result['F1'], metrics_result['F2'], metrics_result['ACC_overall'],
#              metrics_result['IoU_poly'], metrics_result['IoU_bg'], metrics_result['IoU_mean']))


# if __name__ == '__main__':

#     if opt.mode == 'test':
#         print('--- PolypSeg Test---')
#         test()

#     print('Done')
import torch
from tqdm import tqdm
from opt import opt
from utils.metrics import evaluate
import datasets
from torch.utils.data import DataLoader
from utils.comm import generate_model
from utils.metrics import Metrics
import numpy as np
import tifffile
import cv2
import time


def test():
    print('loading data......')
    test_data = getattr(datasets, opt.dataset)(opt.root, opt.test_data_dir, mode='test')
    test_dataloader = DataLoader(test_data, batch_size=1, shuffle=False, num_workers=opt.num_workers)
    total_batch = int(len(test_data) / 1)
    model = generate_model(opt)

    model.eval()

    # metrics_logger initialization
    metrics = Metrics(['recall', 'specificity', 'precision', 'F1', 'F2',
                       'ACC_overall', 'IoU_poly', 'IoU_bg', 'IoU_mean'])
    #time_sum = 0
    time_taken = []
    with torch.no_grad():
        bar = tqdm(enumerate(test_dataloader), total=total_batch)
        for i, data in bar:
            img, gt = data['image'], data['label']
            #name = gt.split("/")[-1].split(".")[0]
            
            if opt.use_gpu:
                img = img.cuda()
                gt = gt.cuda()
            time_start = time.time()
            output,out2,out3, out4,out5= model(img)
            time_end = time.time()
            # End timer
            end_time = time.time() - time_start

            time_taken.append(end_time)
            # time_sum = time_sum+(time_end-time_start)
            # print(output.shape)
            # pass
            _recall, _specificity, _precision, _F1, _F2, \
            _ACC_overall, _IoU_poly, _IoU_bg, _IoU_mean = evaluate(output, gt)

            output = output.detach().squeeze().cpu().numpy()
            out2 = out2.detach().squeeze().cpu().numpy()
            out3 = out3.detach().squeeze().cpu().numpy()
            out4 = out4.detach().squeeze().cpu().numpy()
            out5 = out5.detach().squeeze().cpu().numpy()

            out2= out2 >=0.5
            out3= out3>=0.5
            out4= out4>=0.5
            out5= out5>=0.5
            output= output>=0.5

            out2= out2*255
            out3= out3*255
            out4= out4*255
            out5= out5*255
            output= output*255

            
            ori_img = img.detach().squeeze().cpu().numpy()            
            ori_gt = gt.detach().squeeze().cpu().numpy() 
            ori_gt = ori_gt * 255
            #image  = data[0].cpu().detach().numpy()
            #mask   = target[0].cpu().detach().numpy()
            # cv2.imwrite(f'predictions/etis/exp1/etisprd{i}.png',output)
            # cv2.imwrite(f'predictions/etis/exp1/etisgt{i}.png',ori_gt)

            # cv2.imwrite(f'predictions/cvc300/exp1/cvc300prd{i}.png',output)
            # cv2.imwrite(f'predictions/cvc300/exp1/cvc300gt{i}.png',ori_gt)

            # cv2.imwrite(f'predictions/cvcclinic/exp1/cvcclinicprd{i}.png',output)
            # cv2.imwrite(f'predictions/cvcclinic/exp1/cvcclinicgt{i}.png',ori_gt)

            # cv2.imwrite(f'predictions/cvccolon/exp1/cvccolonprd{i}.png',output)
            # cv2.imwrite(f'predictions/cvccolon/exp1/cvccolongt{i}.png',ori_gt)

            cv2.imwrite(f'predictions/kvasir/exp1/kvasirprd{i}.png',output)
            cv2.imwrite(f'predictions/kvasir/exp1/kvasirgt{i}.png',ori_gt)

            # cv2.imwrite(f'/media/zaka/92A816A5A81687BD/PaperCoding/ACSNet-master/sample_predictions/Endoscan/EndoScansiscial/out2/{i}.png',out2)
            # cv2.imwrite(f'/media/zaka/92A816A5A81687BD/PaperCoding/ACSNet-master/sample_predictions/Endoscan/EndoScansiscial/out3/{i}.png',out3)
            # cv2.imwrite(f'/media/zaka/92A816A5A81687BD/PaperCoding/ACSNet-master/sample_predictions/Endoscan/EndoScansiscial/out4/{i}.png',out4)
            # cv2.imwrite(f'/media/zaka/92A816A5A81687BD/PaperCoding/ACSNet-master/sample_predictions/Endoscan/EndoScansiscial/out5/{i}.png',out5)

            #cv2.imwrite(f'/media/zaka/92A816A5A81687BD/PaperCoding/ACSNet-master/sample_predictions/kavsirown/images/{i}.png',ori_img)
            

            metrics.update(recall= _recall, specificity= _specificity, precision= _precision, 
                            F1= _F1, F2= _F2, ACC_overall= _ACC_overall, IoU_poly= _IoU_poly, 
                            IoU_bg= _IoU_bg, IoU_mean= _IoU_mean
                        )
            
    metrics_result = metrics.mean(total_batch)

    print("Test Result:")
    print('recall: %.4f, specificity: %.4f, precision: %.4f, F1: %.4f, F2: %.4f, '
          'ACC_overall: %.4f, IoU_poly: %.4f, IoU_bg: %.4f, IoU_mean: %.4f'
          % (metrics_result['recall'], metrics_result['specificity'], metrics_result['precision'],
             metrics_result['F1'], metrics_result['F2'], metrics_result['ACC_overall'],
             metrics_result['IoU_poly'], metrics_result['IoU_bg'], metrics_result['IoU_mean']))
    # print('Running time {:.5f}'.format(time_sum/i))
    # print('Average speed: {:.4f} fps'.format(i/time_sum))
    mean_time_taken = np.mean(time_taken)
    mean_fps = 1/mean_time_taken
    print("Mean FPS: ", mean_fps)

if __name__ == '__main__':

    if opt.mode == 'test':
        print('--- PolypSeg Test---')
        test()

    print('Done')