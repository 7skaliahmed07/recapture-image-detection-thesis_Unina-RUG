# Pipeline Summary

- **experiment**: Experiment - 14
- **seed**: 42
- **img_size**: 224
- **batch_size**: 16
- **repeat_factor**: 4
- **augmentation**: ['random_flip_left_right', 'random_brightness(0.1)', 'random_contrast(0.9,1.1)']
- **preprocessing**: none
- **model**: ResNet50(include_top=False) + GAP + Dropout(0.4) + Dense(128,relu) + Dense(1,sigmoid)
- **optimizer**: Adam(0.0001)
- **loss**: binary_crossentropy
- **metrics**: ['accuracy']
- **split**: {'train_frac': 0.85, 'test_frac': 0.15}
- **hyperparameters**: {'learning_rate': 0.0001, 'batch_size': 16, 'optimizer': 'Adam', 'epochs': 8, 'n_folds': 3, 'dropout_rate': 0.4, 'large_size': 256, 'repeat_factor': 4, 'num_test_patches': 5}
