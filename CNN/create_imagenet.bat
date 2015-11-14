SET GLOG_logtostderr=1

"convert_imageset.exe" ../ train.txt imagenet_train_leveldb 1

"convert_imageset.exe" ../ val.txt imagenet_val_leveldb 1