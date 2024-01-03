

Content: 
1. Functional APIs 
2. Custom Loss Function 
3. Custom Layers 
4. Custom Models 
5. Callbacks 

Key-Terms :: 

1. Contrastive Loss 
2. Huber Loss 
3. Custom Loss Function 
4. Siamese Neural Networks 
5. Eucledian Distance 
6. Root Mean Squared Error 

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

## Week-3 

- Every Custom Layer needs to have 3 methods 
1. __init__
2. build 
3. call 



