#!/usr/bin/env python
# Created by "Thieu" at 22:21, 05/10/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from matplotlib import pyplot as plt


def plot_train_history(history, title, pathsave=None):
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(loss))

    plt.figure()
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("MSE")
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig(f"{pathsave}.png")
    plt.show()


def plot_true_pred(y_true, y_pred, title, pathsave=None):
    size = range(len(y_true))
    plt.plot(size, y_true, 'b', label='True')
    plt.plot(size, y_pred, 'r', linestyle='--', label='Prediction')
    plt.legend(loc="upper right")
    plt.title(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(f"{pathsave}.png")
    plt.show()


def plot_multiple_true_pred(y_true, y_pred, title, pathsave=None):
    fig, a = plt.subplots(3, 1, figsize=(10, 7))

    a[0].plot(y_true[:, 0], "b")
    a[0].plot(y_pred[:, 0], "r")
    a[0].set_ylabel("GNSS_X")
    a[0].legend(labels=["True", "Prediction"], loc="upper right")

    a[1].plot(y_true[:, 1], "b")
    a[1].plot(y_pred[:, 1], "r")
    a[1].set_ylabel('GNSS_Y')
    a[1].legend(labels=["True", "Prediction"], loc="upper right")

    a[2].plot(y_true[:, 2], "b")
    a[2].plot(y_pred[:, 2], "r")
    a[2].set_ylabel('GNSS_Z')
    a[2].legend(labels=["True", "Prediction"], loc="upper right")

    plt.suptitle(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(f"{pathsave}.png")
    plt.show()