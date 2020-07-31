# -*- coding: utf-8 -*-
# iris_minimal.py
# PyTorch 1.5.0-CPU Anaconda3-2020.02 Python 3.7.6
# Windows 10
import numpy as np
import torch as T

device = T.device("cpu")  # to Tensor or Module

# -------------------------------------------------


class Net(T.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hid1 = T.nn.Linear(4, 7)  # 4-7-3
        self.oupt = T.nn.Linear(7, 3)
        # (initialize weights)

    def forward(self, x):
        z = T.tanh(self.hid1(x))
        z = self.oupt(z)  # see CrossEntropyLoss()
        return z


def saveModel():
    print("\nEnd Iris demo")


def evalulateMOdel(net):
    net.eval()
    print("\nPredicting for [5.8, 2.8, 4.5, 1.3]: ")
    unk = np.array([[5.8, 2.8, 4.5, 1.3]],
                   dtype=np.float32)
    unk = T.tensor(unk, dtype=T.float32).to(device)
    logits = net(unk).to(device)
    probs = T.softmax(logits, dim=1)
    probs = probs.detach().numpy()  # nicer printing
    np.set_printoptions(precision=4)

    print(probs)


def trainModel(net, train_x, train_y):
    max_epochs = 100
    lrn_rate = 0.04
    loss_func = T.nn.CrossEntropyLoss()
    optimizer = T.optim.SGD(net.parameters(),    lr=lrn_rate)

    print("\nStarting training ")
    net.train()
    indices = np.arange(6)

    for epoch in range(0, max_epochs):
        np.random.shuffle(indices)
        for i in indices:
            X = train_x[i].reshape(1, 4)
            Y = train_y[i].reshape(1,)
            optimizer.zero_grad()
            oupt = net(X)
            loss_obj = loss_func(oupt, Y)
            loss_obj.backward()
            optimizer.step()

    # (monitor error)
    print("Done training ")


def trainingData():
    print("\nLoading Iris train data ")

    train_x = np.array([
        [5.0, 3.5, 1.3, 0.3],
        [4.5, 2.3, 1.3, 0.3],
        [5.5, 2.6, 4.4, 1.2],
        [6.1, 3.0, 4.6, 1.4],
        [6.7, 3.1, 5.6, 2.4],
        [6.9, 3.1, 5.1, 2.3]], dtype=np.float32)

    train_y = np.array([0, 0, 1, 1, 2, 2],
                       dtype=np.long)

    print("\nTraining predictors:")
    print(train_x)
    print("\nTraining class labels: ")
    print(train_y)

    train_x = T.tensor(train_x,
                       dtype=T.float32).to(device)
    train_y = T.tensor(train_y,
                       dtype=T.long).to(device)
    return train_x, train_y


def getStarted():
    # 0. get started
    print("\nBegin minimal PyTorch Iris demo ")
    T.manual_seed(1)
    np.random.seed(1)

# -------------------------------------------------
def main():
    # 0. get started
    getStarted()

    # 1. set up training data
    train_x, train_y = trainingData()

    # 2. create network
    net = Net().to(device)  # or Sequential()

    # 3. train model
    trainModel(net, train_x, train_y)

    # 4. (evaluate model accuracy)
    # 5. use model to make a prediction
    evalulateMOdel(net)

    # 6. (save model)
    saveModel()


if __name__ == "__main__":
    main()
