from scripts.dss_model import load_model, predict_img, get_class_label

if __name__ == "__main__":
    model = load_model()
    classes = predict_img("C:\\Users\DELL\OneDrive\Desktop/brown.png", model)
    label = get_class_label(classes)
    print(label)
