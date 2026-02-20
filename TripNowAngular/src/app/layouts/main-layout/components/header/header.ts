import {Component, signal} from '@angular/core';

import {RouterLink} from "@angular/router";
import {Qr} from "../qr/qr";


@Component({
  selector: 'app-header',
  imports: [

    RouterLink,
    Qr
  ],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {

  usuarioLoggeado = signal<boolean>(true)

  abrirQR = signal<boolean>(false);


  toggleQR(){
    this.abrirQR.update(state => !state)
  }


  idiomaElegido = signal('Español');

  elegirIdioma(e: string) {
    this.idiomaElegido.set(e);
  }





  constructor() {
  }

}
