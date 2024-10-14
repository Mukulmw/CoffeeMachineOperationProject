
# Coffee Machine Project

This is a simple console-based Coffee Machine program written in Python. The user can order drinks such as espresso, latte, or cappuccino, and the machine will check if there are enough resources (water, coffee, and milk) to make the drink. The user is required to insert coins, and the program calculates whether the amount is sufficient for the drink and dispenses change if necessary.

## Features
- **Drinks Available**: Espresso, Latte, Cappuccino.
- **Resource Check**: Ensures there is enough water, coffee, and milk to prepare the selected drink.
- **Coin Processing**: The user can input quarters, dimes, nickels, and pennies to pay for the drink.
- **Change Calculation**: If the user inputs more money than required, the program returns the correct change.
- **Reports**: The machine can generate a report of remaining resources and total money earned.
- **Turn Off**: The machine can be turned off with a command.

## How to Use
1. Run the program.
2. When prompted with `What would you like? (espresso/latte/cappuccino)`, type in the drink you want:
   - `espresso`
   - `latte`
   - `cappuccino`
3. If you want to see the resources and earnings report, type `report`.
4. To turn off the machine, type `off`.

### Example Interaction:
```
What would you like? (espresso/latte/cappuccino): latte
Please insert the coins!
Please insert quarters: 10
Please insert dimes: 2
Please insert nickles: 0
Please insert pennies: 4
Here's your change: 0.54
```

### Commands:
- **`off`**: Turn the machine off.
- **`report`**: See the report of resources (water, milk, coffee) and total money collected.

## Program Structure

1. **MENU**: Contains details about drinks, ingredients, and their cost.
2. **resources**: Tracks available quantities of water, milk, and coffee.
3. **money**: Tracks the total earnings of the machine.
4. **Functions**:
   - `check_resources(drink)`: Checks if the required resources are available to make the drink.
   - `turn_off()`: Turns off the coffee machine.
   - `report()`: Prints a report of the available resources and money earned.
   - `reduce_resources(drink)`: Deducts the ingredients used from the available resources.
   - `process_coins(quarters, dimes, nickles, pennies, drink)`: Processes the coins inserted by the user and checks if sufficient money was provided.
5. **Main Loop**: The program keeps running until the user enters `off` to turn it off.

## Error Handling
- If there are not enough resources to make a drink, the program informs the user and doesn't proceed.
- If insufficient money is provided, the program refunds the money and informs the user.
