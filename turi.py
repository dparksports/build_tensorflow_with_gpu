import turicreate as tc
images = tc.image_analysis.load_images("dataset")
annotations = tc.SFrame.read_json("dataset/annotations.json")
joined_sframe = images.join(annotations)
training_sframe, testing_sframe = joined_sframe.random_split(0.8)
training_sframe
testing_sframe
model_50 = tc.object_detector.create(training_sframe, max_iterations=50)
model_50