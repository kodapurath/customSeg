# customSeg
A plug and play framework to implement different backbones and decoders for semantic segmentation(credits: [Bonnetal!](https://github.com/PRBonn/bonnetal))

## Directory structure
Create a dataset folder and store Cityscapes data in it

![image](https://user-images.githubusercontent.com/25299756/121074188-23680f00-c7f1-11eb-86fc-6759641d4f30.png)

## To evaluate on training set
```./train.py -c config/cityscapes/cityscapes_darknet53_aspp_2048_os8_76/cfg.yaml -p config/cityscapes/cityscapes_darknet53_aspp_2048_os8_76/ -l config/cityscapes/cityscapes_darknet53_aspp_2048_os8_76/log/ --eval```

## To infer a single image
```./infer_img.py -p config/cityscapes/cityscapes_darknet53_aspp_2048_os8_76/ -i dataset/cityscapes/leftImg8bit/test/berlin/berlin_000018_000019_leftImg8bit.png -v```

## Pre-Trained models for Cityscapes Dataset
[DarkNet53 ASPP - 1024x2048px](http://ipb.uni-bonn.de/html/projects/bonnetal/segmentation/cityscapes_darknet53_aspp_2048_os8_76.tar.gz)

[MobilenetsV2 ASPP - 512x1024px](http://ipb.uni-bonn.de/html/projects/bonnetal/segmentation/cityscapes_mobilenetsv2_aspp_1024_os8_70.tar.gz)

[MobilenetsV2 ASPP Residual- 512x1024px](http://ipb.uni-bonn.de/html/projects/bonnetal/segmentation/cityscapes_mobilenetsv2_aspp_res_1024_os8_70.tar.gz)

For more pre-trained models visit [Bonnetal!](https://github.com/PRBonn/bonnetal)
