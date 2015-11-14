rd /S /Q imagenet_train_leveldb
rd /S /Q imagenet_val_leveldb
create_imagenet.bat
DEL /Q imagenet_mean.binaryproto
make_imagenet_mean.bat
run_train_imagenet.bat