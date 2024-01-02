


# Week-2 

- Custom Loss Function 

- Using Loss Function 

```
model.compile(loss='mse', optimizer='sgd')
```

The above can also be declared as:

```
from tensorflow.keras.losses import mean_squared_error 
model.compile(loss=mean_squared_error, optimizer='sgd')

```

## Creating a Custom Loss Function 

```
def my_loss_function(y_true, y_pred):
    return loss
```
