import { Component,OnInit , signal} from '@angular/core';
import {ViajesService} from "../../core/services/viajes/viajes.service";

import {AlertasService} from "../../core/utils/alertas.service";
import {NgClass} from "@angular/common";



interface ReseniasInterface {
  identificador: string;
  alojamiento: string;
  slug_resenia: string;
  descripcion: string;
  puntuacion: number;
  imagen: string;
  usuario: string;

}



@Component({
  selector: 'app-resenias',
  imports: [
    NgClass

  ],
  templateUrl: './resenias.html',
  styleUrl: './resenias.scss',
})
export class Resenias implements OnInit{
  resenias = signal<ReseniasInterface[]>([])



  constructor(
      private viajesService: ViajesService,
      private alertasService: AlertasService,
  ) {
  }

  ngOnInit() {
    this.alertasService.showLoader()
    setTimeout(() => {
      this.viajesService.getResenias().subscribe({
        next: response => {
          this.resenias.set(response.data);
        },

        error: error => {
          console.log(error);

        },
        complete: () => {
          this.alertasService.hide()
        }
      })
    })

    this.viajesService.getResenias().subscribe({
      next: response => {
        this.resenias.set(response.data);
      },
      error: error => {
        console.log(error);
      }
    })


  }

  estrellas: number[]= [1,2,3,4,5];
}


