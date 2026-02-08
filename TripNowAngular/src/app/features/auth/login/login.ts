import { Component } from '@angular/core';

@Component({
    selector: 'app-login',
    imports: [],
    templateUrl: './login.html',
    styleUrl: './login.scss',
    standalone: true
})
export class Login {


  TogglePassword(elementPresionado: any){

    const divPadre = elementPresionado.parentNode;
    const input = divPadre.querySelector('input');
    const icon = elementPresionado.querySelector('i');

    input.type = input.type === 'password' ? 'text' : 'password';

    if (icon.classList.contains("bi-eye-fill")){
        icon.classList.remove("bi-eye-fill");
        icon.classList.add("bi-eye-slash-fill");
    }
    else {
        icon.classList.remove("bi-eye-slash-fill");
        icon.classList.add("bi-eye-fill");
    }
  }

  mostrarRegistro = false;


}

