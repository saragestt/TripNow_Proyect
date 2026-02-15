import {Component, OnInit, signal} from '@angular/core';
import {NgClass} from "@angular/common";
import {ViajesService} from "../../core/services/viajes/viajes.service";
import {AlertasService} from "../../core/utils/alertas.service";


interface ViajesInterface {
  identificador: string;
  ciudad_salida: string;
  ciudad_llegada: string;
  terminal_salida: string;
  terminal_llegada: string;
  lugar_salida: string;
  lugar_llegada: string;
  fecha_salida: string;
  fecha_llegada: string;
  precio: number;
  nombre_categoria: string;
  slug_categoria: string;
  slug_viaje: string;
  imagen: string;
}

interface CategoriasInterface {
  nombre: string;
  slug: string;
}



@Component({
  selector: 'app-busquedas',
  imports: [
      NgClass
  ],
  templateUrl: './busquedas.html',
  styleUrl: './busquedas.scss',
  standalone: true
})

export class Busquedas implements OnInit{
  viajes = signal<ViajesInterface[]>([])


  categorias = signal<CategoriasInterface[]>([])

  constructor(
      private viajesService: ViajesService,
      private alertasService: AlertasService,
  ) {
  }

  ngOnInit() {
    this.alertasService.showLoader()
    setTimeout(() => {
      this.viajesService.getViajes().subscribe({
        next: response => {
          this.viajes.set(response.data);
        },

        error: error => {
          console.log(error);

        },
        complete: () => {
          this.alertasService.hide()
        }
      })

      this.viajesService.getCategorias().subscribe({
        next: response => {
          this.categorias.set(response.data);

        },
        error: error => {
          console.log(error);
        }
      })


    }, 1500)

  }
  optCategoria: string = "todos"

  changeCategory(slug: string) {

    if (this.optCategoria === slug) {
      this.optCategoria = "todos";
    }
    else {
      this.optCategoria = slug;
    }
  }


}
