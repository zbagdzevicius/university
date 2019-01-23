package first.second.third.controllers;

import first.second.third.beans.documents.User;
import first.second.third.beans.response.UserResponse;
import first.second.third.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController

@RequestMapping(value = "/user")
@CrossOrigin
public class UserController {

    @Autowired
    private UserService service;

    @GetMapping
    public List<UserResponse> getAllUser() {
        return service.getAllUser();
    }

    @PostMapping(value = "/register")
    public UserResponse addUser(@Valid @RequestBody User user) {
        return new UserResponse(service.addNewUser(user));
    }

    @DeleteMapping(value = "/deleteAll")
    public void deleteAllUsers() {
        service.deleteAllUsers();
    }

    @PostMapping(value = "/login")
    public String login(
            @RequestParam("userName") String userName,
            @RequestParam("password") String password) {
        return service.login(userName, password);
    }

    @PostMapping(value = "/auth")
    public String auth(@RequestParam("accessToken") String accessToken){
        return service.authenticate(accessToken);
    }


}
