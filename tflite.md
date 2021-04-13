## tflite conversion from Resnet50

```sh

python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config

python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config --checkpoint_dir=models/my_ssd_resnet50_v1_fpn

python exporter_main_v2.py --input_type=image_tensor --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config --trained_checkpoint_dir=models/my_ssd_resnet50_v1_fpn --output_directory=exported-models/my_model_at_ckpt_2000

python ../models/research/object_detection/export_tflite_graph_tf2.py --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config --trained_checkpoint_dir=models/my_ssd_resnet50_v1_fpn --output_directory tflite

tflite_convert --saved_model_dir=tflite/saved_model --output_file=tflite/model.tflite

```
