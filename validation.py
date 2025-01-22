from ultralytics import YOLO

# Load a model
model = YOLO(r".\runs\detect\train\weights\best.pt")

# Validate with a custom dataset

metrics = model.val(data="./config.yaml")
metrics.box.map50  # map50
metrics.box.maps  # a list contains map50-95 of each category

# Replot the results
model.plot_results()