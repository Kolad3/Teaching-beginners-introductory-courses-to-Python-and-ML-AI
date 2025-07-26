def predict_mood():
    sleep = input("did you sleep well? (yes/no): ")
    eat = input("Did you eat breakfast? (yes/no): ")
    tired = input('Are you feeling tired? (yes/no): ')

    if sleep == 'yes' and tired == 'no':
        print("You're energetic and ready to go!")
    elif sleep == 'no' and tired == 'yes':
        print('You seem tired. Getsome rest soon')
    else:
        print('A bit drained. Take care of yourself!')

predict_mood()