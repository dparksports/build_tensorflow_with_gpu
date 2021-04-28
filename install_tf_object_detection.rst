TensorFlow Object Detection API Installation
--------------------------------------------

Now that you have installed TensorFlow, it is time to install the TensorFlow Object Detection API.

Downloading the TensorFlow Model Garden
***************************************

- Create a new folder under a path of your choice and name it ``TensorFlow``.
- From your `Terminal` ``cd`` into the ``TensorFlow`` directory.
- To download the models you can either use `Git <https://git-scm.com/downloads>`_ to clone the `TensorFlow Models repository <https://github.com/tensorflow/models>`_ inside the ``TensorFlow`` folder, or you can simply download it as a `ZIP <https://github.com/tensorflow/models/archive/master.zip>`_ and extract its contents inside the ``TensorFlow`` folder. To keep things consistent, in the latter case you will have to rename the extracted folder ``models-master`` to ``models``.
- You should now have a single folder named ``models`` under your ``TensorFlow`` folder, which contains another 4 folders as such:

.. code-block:: default

    TensorFlow/
    └─ models/
       ├─ community/
       ├─ official/
       ├─ orbit/
       ├─ research/
       └── ...

Protobuf Installation/Compilation
*********************************

The Tensorflow Object Detection API uses Protobufs to configure model and
training parameters. Before the framework can be used, the Protobuf libraries
must be downloaded and compiled. 

This should be done as follows:

- Head to the `protoc releases page <https://github.com/google/protobuf/releases>`_
- Download the latest ``protoc-*-*.zip`` release (e.g. ``protoc-3.12.3-win64.zip`` for 64-bit Windows)
- Extract the contents of the downloaded ``protoc-*-*.zip`` in a directory ``<PATH_TO_PB>`` of your choice (e.g. ``C:\Program Files\Google Protobuf``)
- Add ``<PATH_TO_PB>`` to your ``Path`` environment variable (see :ref:`set_env`)
- In a new `Terminal` [#]_, ``cd`` into ``TensorFlow/models/research/`` directory and run the following command:

    .. code-block:: default

        # From within TensorFlow/models/research/
        protoc object_detection/protos/*.proto --python_out=.

.. important::

    If you are on Windows and using Protobuf 3.5 or later, the multi-file selection wildcard (i.e ``*.proto``) may not work but you can do one of the following:

    .. tabs::

        .. tab:: Command Prompt

            .. code-block:: default

                    # From within TensorFlow/models/research/
                    for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.


.. _tf_models_install_coco:

COCO API installation
*********************

As of TensorFlow 2.x, the ``pycocotools`` package is listed as `a dependency of the Object Detection API <https://github.com/tensorflow/models/blob/master/research/object_detection/packages/tf2/setup.py>`_. Ideally, this package should get installed when installing the Object Detection API as documented in the :ref:`tf_models_install_object_detection` section below, however the installation can fail for various reasons and therefore it is simpler to just install the package beforehand, in which case later installation will be skipped.

    .. tab:: Linux

        Download `cocoapi <https://github.com/cocodataset/cocoapi>`_ to a directory of your choice, then ``make`` and copy the pycocotools subfolder to the ``Tensorflow/models/research`` directory, as such:

        .. code-block:: default

            git clone https://github.com/cocodataset/cocoapi.git
            cd cocoapi/PythonAPI
            make
            cp -r pycocotools <PATH_TO_TF>/TensorFlow/models/research/

.. note:: The default metrics are based on those used in Pascal VOC evaluation.

    - To use the COCO object detection metrics add ``metrics_set: "coco_detection_metrics"`` to the ``eval_config`` message in the config file.

    - To use the COCO instance segmentation metrics add ``metrics_set: "coco_mask_metrics"`` to the ``eval_config`` message in the config file.


.. _tf_models_install_object_detection:

Install the Object Detection API
********************************
Installation of the Object Detection API is achieved by installing the ``object_detection`` package. This is done by running the following commands from within ``Tensorflow\models\research``:

.. code-block:: default

    # From within TensorFlow/models/research/
    cp object_detection/packages/tf2/setup.py .
    python -m pip install .

.. _test_tf_models:

Test your Installation
**********************

To test the installation, run the following command from within ``Tensorflow\models\research``:

.. code-block:: default

    # From within TensorFlow/models/research/
    python object_detection/builders/model_builder_tf2_test.py

Once the above is run, allow some time for the test to complete and once done you should observe a
printout similar to the one below:

.. code-block:: default

    ...
    [       OK ] ModelBuilderTF2Test.test_create_ssd_models_from_config
    [ RUN      ] ModelBuilderTF2Test.test_invalid_faster_rcnn_batchnorm_update
    [       OK ] ModelBuilderTF2Test.test_invalid_faster_rcnn_batchnorm_update
    [ RUN      ] ModelBuilderTF2Test.test_invalid_first_stage_nms_iou_threshold
    [       OK ] ModelBuilderTF2Test.test_invalid_first_stage_nms_iou_threshold
    [ RUN      ] ModelBuilderTF2Test.test_invalid_model_config_proto
    [       OK ] ModelBuilderTF2Test.test_invalid_model_config_proto
    [ RUN      ] ModelBuilderTF2Test.test_invalid_second_stage_batch_size
    [       OK ] ModelBuilderTF2Test.test_invalid_second_stage_batch_size
    [ RUN      ] ModelBuilderTF2Test.test_session
    [  SKIPPED ] ModelBuilderTF2Test.test_session
    [ RUN      ] ModelBuilderTF2Test.test_unknown_faster_rcnn_feature_extractor
    [       OK ] ModelBuilderTF2Test.test_unknown_faster_rcnn_feature_extractor
    [ RUN      ] ModelBuilderTF2Test.test_unknown_meta_architecture
    [       OK ] ModelBuilderTF2Test.test_unknown_meta_architecture
    [ RUN      ] ModelBuilderTF2Test.test_unknown_ssd_feature_extractor
    [       OK ] ModelBuilderTF2Test.test_unknown_ssd_feature_extractor
    ----------------------------------------------------------------------
    Ran 20 tests in 68.510s

    OK (skipped=1)

Try out the examples
********************
If the previous step completed successfully it means you have successfully installed all the
components necessary to perform object detection using pre-trained models.

If you want to play around with some examples to see how this can be done, now would be a good
time to have a look at the :ref:`examples` section.
