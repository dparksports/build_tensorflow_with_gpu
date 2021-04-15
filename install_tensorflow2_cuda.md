# How to install Tensorflow2 with GPU support

Installation of Tensorflow2 with GPU support is easy and the only complication can be arisen from the CUDA compability which in turns depends on the Nvidia driver version. Before going farther, please check if your Nvidia Video Card is compatible with the required versions that are defined in this gist, use this [link](https://www.nvidia.com/Download/index.aspx). 

Tensorflow offers in its website a table of the compatibility between libraries for the target OS. You can visit that website in the following [link](https://www.tensorflow.org/install/source) that points to the Tensorflow installation from source for linux (CUDNN version is wrong, the correct one is 7.6.5 as we will se later).  

For the time writing this gist, Tensorflow2 requires from CUDA version 10.0 and CUDNN 7.6.5. It is really important to match the exact version, otherwise tensorflow will have problems loading the shared libraries as not finding the correct version. 

As commented previously, CUDA version also requires for a minimum Nvidia driver version. In our case, CUDA 10.0 requires from Nvidia driver superior to 410.48 and you can check that information from CUDA website that can be found in this [link](https://docs.nvidia.com/deploy/cuda-compatibility/index.html). 

## Proceed with the installation of the CUDA TOOLKIT

For the CUDA installation we must visit Cuda website and select the exact version 10.0. Nowadays, it is even not the latest one so you have to navigate through the legacy releases to find the exact version. If you do not find the correct link, google it, anyway I've attached the current [link](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=debnetwork) to include the repository to install CUDA 10.0 but using the following configuration defined in the website `Linux > x86_64 > Ubunut > 18.04 > deb(network)`

Download the .deb file and run the following installation instructions offered by CUDA:

    $ sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
    $ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub 
    $ sudo apt-get update
    $ sudo apt-get install cuda-toolkit-10-0 //Be aware!! I have change this line to only install the respective toolkit.

Important, before installing *cuda* package make sure that this package is not upgrading your Nvidia drivers, otherwise it would mess up the installation. In fact, we only want to install the CUDA Toolkit not the CUDA package that contains the toolkit and the Nvidia drivers. If you want to do not fail this step launch the proposed sentence: ´sudo apt-get install cuda-toolkit-10-0´

**Possible Errors**: If you have problems installing cuda-repo-ubuntu...deb because you have previously installed versions of cuda, you can find the previous packages using ´dpkg -l | grep cuda*´ and delete them with ´dpkg -r package_name´.

## Install CUDNN

It is really easy. You only have to download the CUDNN version from Nvidia (you must create an account for the CUDNN download) through this [link](https://developer.nvidia.com/rdp/cudnn-download). In the website look for the CUDNN version compatible with CUDA 10.0. In fact, the version is 7.6.5, so proceed to download cuDNN Library for Linux.

Next steps are really well explained by LearnOpenCV blog in the following post [*Installing Deep Learning Frameworks on Ubuntu with CUDA support*](https://www.learnopencv.com/installing-deep-learning-frameworks-on-ubuntu-with-cuda-support/). Basically, we have to uncompress the file and copy the extracted libs to the cuda installation folder. 

    $ tar xvf cudnn-8.0-linux-x64-v6.0.tgz
    $ sudo cp -P cuda/lib64/* /usr/local/cuda/lib64/
    $ sudo cp cuda/include/* /usr/local/cuda/include/

Now, we have to configure some enviroment variables to help the system locate these libraries:

    $ echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"' >> ~/.bashrc
    $ echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc
    $ echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> ~/.bashrc

Reload the file:

    $ source ~/.bashrc

## Install Tensorflow2 with GPU

First of all, it is always recommended to use virtual environments. 

Once created the virtual environment, activate it and install Tensorflow using PyPy:
    
    $ pip3 install tensorflow-gpu //By default it will install the latest estable version of Tensorflow; in this case version 2.0.

To check the correct installation import the tensorflow package and run a sequence to test if the GPU is available:

    $ python3 //To enter in the python interpreter
    > import tensorflow as tf
    > tf.test.is_gpu_available()
    
If you sucess you will receive a ´True´ response.

## Mnist example 

    from __future__ import absolute_import, division, print_function, unicode_literals
   
    import tensorflow as tf

    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    model.evaluate(x_test,  y_test, verbose=2)


### Source
- [learnopencv](https://www.learnopencv.com/installing-deep-learning-frameworks-on-ubuntu-with-cuda-support/)
- [tensorflow-install](https://www.tensorflow.org/install/install_linux)
- [tensorflow-versions](https://www.tensorflow.org/versions/)
