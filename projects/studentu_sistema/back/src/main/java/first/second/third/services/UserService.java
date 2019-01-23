package first.second.third.services;

import first.second.third.beans.documents.User;
import first.second.third.beans.response.UserResponse;
import first.second.third.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.validation.Valid;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public List<UserResponse> getAllUser() {
        return userRepository.findAll().stream()
                .map(UserResponse::new)
                .collect(Collectors.toList());
    }

    public void deleteAllUsers() {
        userRepository.deleteAll();
    } // delete all users for testing purposes

    public User addNewUser(@Valid User user) { // register function
        User newUser = new User(); // create currently registering user

        String wantedUsername = user.getUserName(); // get user name
        String wantedEmail = user.getEmail(); // get email

        if (userExist(wantedUsername)) { // check if user with wantedUsername exist
            throw new IllegalArgumentException("Vartotojas su tokiu slapyvardžiu jau egzistuoja"); // thrown exception if userName exist
        } else if (emailExist(wantedEmail)) { // check if user with wantedEmail exist
            throw new IllegalArgumentException("Vartotojas su tokiu elektroniniu paštu jau egzistuoja"); // thrown exception if email exist
        }

        newUser.setId(user.getId()); // set values to currently registering user if valid
        newUser.setEmail(wantedEmail); // using wantedEmail instead of user.getEmail()
        newUser.setFirstName(user.getFirstName());
        newUser.setLastName(user.getLastName());
        newUser.setUserName(wantedUsername);
        newUser.setPassword(user.getPassword());
        newUser.setUniversity(user.getUniversity());

        return userRepository.save(newUser); // save new users
    }

    private boolean userExist(String userName) { // function to check if userNameExist
        String UserInDatabase = userRepository.findUserByUserName(userName); // argument(userName) value in database
        return UserInDatabase != null; // if null(or empty) then userName exist, else doesn't exist
    }

    private boolean emailExist(String email) { // function to check if emailExist
        String UserInDatabase = userRepository.findUserByEmail(email); // argument(email) value in database
        return UserInDatabase != null; // if null(or empty) then email exist, else doesn't exist
    }

    public String login(String userName, String password) {
        if (!userExist(userName)) { // check if user with username exist
            return "Slapyvardis neegzistuoja"; // thrown exception if userName exist
        }
        User loggingUser = userRepository.getUserByUserName(userName); // used to get wanted user object
        String userPassword = loggingUser.getPassword();
        if(password.equals(userPassword)){ // check if right password
           String token = Long.toHexString(Double.doubleToLongBits(Math.random())); // generating access token
           loggingUser.setAccessToken(token);
           userRepository.save(loggingUser);
           return(token);
        };
        return "Netinkamas slaptažodis"; // if wrong password
    }

    public String authenticate(String accessToken){
        String user = userRepository.findUserByAccessToken(accessToken);
        if (user != null) { // check if user with username exist
            return "true";
        }
        return "false";
    }
}
