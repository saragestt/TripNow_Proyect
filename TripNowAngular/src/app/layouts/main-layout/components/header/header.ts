import {Component, signal} from '@angular/core';
import {Idioma} from "../idioma/idioma";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-header',
  imports: [
    Idioma,
    RouterLink
  ],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {

  usuarioLoggeado = signal<boolean>(true)
  openIdioma = signal<boolean>(false);

  toggleIdioma() {
    this.openIdioma.update(state => !state)
  }


  constructor() {
  }

}
