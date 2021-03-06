import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim = 1)
y = x.pow(2) + 0.2 * torch.rand(x.size())

x, y =  Variable(x), Variable(y)
#plt.scatter(x.data.numpy(), y.data.numpy())
#plt.show()

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x


net = Net(1, 10, 1)
opt = torch.optim.SGD(net.parameters(), lr = 0.5)
loss_func = torch.nn.MSELoss()

plt.ion()
plt.show()

for t in range(100):
    prediction = net(x)
    loss = loss_func(prediction, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

    if t % 5 ==0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())#散點圖
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'ro', lw = 5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.item(), fontdict={'size':20, 'color':'red' })
        plt.pause(0.1)
