import { Component } from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";

@Component({
  selector: 'app-autentificacion',
  imports: [
      ReactiveFormsModule,
      FormsModule,
  ],
  templateUrl: './autentificacion.html',
  styleUrl: './autentificacion.scss',
  standalone: true
})
export class Autentificacion {

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
