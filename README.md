# build_tensorflow_with_cuda
Building TensorFlow from source (TF 2.4.1, Ubuntu 20.04)

## Why build from source?
The TensorFlow official instructions: https://www.tensorflow.org/install.

- [pip](https://www.tensorflow.org/install/pip)
    - caution: outdated and may not work with your TF code.
 
 - A good docker alternative
  -   [Docker image](https://www.tensorflow.org/install/docker).

 - caution: These pre-built binaries are often not compatible with the Ubuntu version, the CUDA version, and the TF installed. 
 - These may be slower than binaries optimized for the target architecture (e.g. AVX2, FMA).


## Described configuration

Build TensorFlow in the following configuration:

 - Ubuntu 20.04
 - NVIDIA driver v460.57
 - CUDA 11.0.2 / cuDNN v8.0.2.39
 - GCC 9.3.0 (system default; Ubuntu 9.3.0-10ubuntu2)
 - TensorFlow v2.3.0

## Prerequisites

### Installing the NVIDIA driver, CUDA and cuDNN

- Tensorflow2 with GPU support has only complication of the CUDA compability.
- Tensorflow2 requires from CUDA version 10.0 and CUDNN 7.6.5
- Important: do not upgrade the nvidia driver.  
- Otherwise, this causes the entire installation to be incompatible.

```

   $ sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
    $ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub 
    $ sudo apt-get update
    $ sudo apt-get install cuda-toolkit-10-0 
```
    
## Install CUDNN
[link](https://developer.nvidia.com/rdp/cudnn-download).

```

    $ tar xvf cudnn-8.0-linux-x64-v6.0.tgz
    $ sudo cp -P cuda/lib64/* /usr/local/cuda/lib64/
    
    
    $ sudo cp cuda/include/* /usr/local/cuda/include/
    $ echo 'export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"' >> ~/.bashrc
    $ echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc
    $ echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> ~/.bashrc
    
        $ source ~/.bashrc
```
	
## Install Tensorflow2 with GPU

activate a virtual environment

```
    $ pip install virtualenv
    $ virtualenv --version
     $ cd projectFolder
    $ virtualenv projectName   
      $ source projectFolder/bin/activate
      
          $ pip3 install tensorflow-gpu 
	  
	      $ python3 //To enter in the python interpreter
    > import tensorflow as tf
    > tf.test.is_gpu_available()
```

### System packages

    $ sudo apt install python3-dev python3-pip python3-venv

## Installing Bazel

[Bazel](https://bazel.build/) is Google's monster of a build system and is required to build TensorFlow.

TensorFlow 2.3.0 now requires Bazel 3.1.0


### Installing Bazel via apt
(https://docs.bazel.build/versions/master/install-ubuntu.html#install-on-ubuntu:
Bazel needs to be built using Bazel.

```
$ sudo apt install curl gnupg
$ curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
$ echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
$ sudo apt update && sudo apt install bazel-3.1.0
```

Use this version: `bazel-3.1.0`  otherwise tf won't compile.

### Compiling Bazel from source
(https://docs.bazel.build/versions/master/install-compile-source.html).

install some prerequisite dependencies:

```
sudo apt-get install build-essential openjdk-11-jdk python zip unzip
```


```
$ wget https://github.com/bazelbuild/bazel/releases/download/3.1.0/bazel-3.1.0-dist.zip
$ mkdir bazel-3.1.0
$ unzip -d ./bazel-3.1.0 bazel-3.1.0-dist.zip
```

```
$ cd bazel-3.1.0
$ env EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" bash ./compile.sh
```
The binary should be located in `output/` 
Add it to `PATH`.

## Building TensorFlow

### Cloning and patching

      $ git clone https://github.com/tensorflow/tensorflow
      $ cd tensorflow
      $ git checkout v2.4.1

### Configuration


      $ python3 -m venv ~/.virtualenvs/tf_dev

 `source ~/.virtualenvs/tf_dev/bin/activate`. 

Install the Python packages(https://www.tensorflow.org/install/source):

    $ pip install -U pip six 'numpy<1.19.0' wheel setuptools mock 'future>=0.17.1'
    $ pip install -U keras_applications --no-deps
    $ pip install -U keras_preprocessing --no-deps



TensorFlow configuration script

      $ ./configure

      CUDA support -> Y

### Building

	$ bazel build --config=opt -c opt //tensorflow/tools/pip_package:build_pip_package
    
* Add `-c dbg --strip=never` for debugging purposes).
* Add `--compilation_mode=dbg` to build in debug without optimizations.  Shouldn't do this



### Building & installing the Python package

      $ ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

      $ pip install /tmp/tensorflow_pkg/tensorflow-2.3.0-cp38-cp38-linux_x86_64.whl

### Testing the installation

    $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    
    run mnist in python to verify the convergence.
    
## Mnist example 

```python

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
    
 ```

    ### Source
- [tensorflow-install](https://www.tensorflow.org/install/install_linux)
- [tensorflow-versions](https://www.tensorflow.org/versions/)
