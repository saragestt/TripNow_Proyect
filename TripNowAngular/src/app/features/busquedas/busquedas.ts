import {Component, OnInit, signal} from '@angular/core';
import {NgClass, NgForOf} from "@angular/common";
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

interface CategoriasAlojamientosInterface {
  nombre: string;
  slug: string;

}

interface AlojamientosInterface {
  identificador: string;
  nombre_alojamiento: string;
  fecha_llegada: string;
  fecha_salida: string;
  ciudad: string;
  precio: number;
  nombre_categoria_alojamiento: string;
  slug_categoria_alojamiento: string;
  slug_alojamiento: string;
  imagen: string;
}




@Component({
  selector: 'app-busquedas',
  imports: [
    NgClass,
    NgForOf
  ],
  templateUrl: './busquedas.html',
  styleUrl: './busquedas.scss',
  standalone: true
})

export class Busquedas implements OnInit{
  viajes = signal<ViajesInterface[]>([])
  categorias = signal<CategoriasInterface[]>([])

  categorias_alojamiento = signal<CategoriasAlojamientosInterface[]>([])

  alojamientos = signal<AlojamientosInterface[]>([])



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

      this.viajesService.getAlojamientos().subscribe({
        next: response => {
          this.alojamientos.set(response.data);
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

      this.viajesService.getCategoriasAlojamiento().subscribe({
        next: response => {
          this.categorias_alojamiento.set(response.data);
        },
        error: error => {
          console.log(error);
        }
      })


    }, 400)

  }
  elegir_categoria_viaje: string = "todos"
  elegir_categoria_alojamiento: string = "todos"

  cambiarCategoriaViaje(slug: string) {

    if (this.elegir_categoria_viaje === slug) {
      this.elegir_categoria_viaje = "todos";
    }
    else {
      this.elegir_categoria_viaje = slug;
    }
  }

  cambiarCategoriaAlomiento(slug: string) {

    if (this.elegir_categoria_alojamiento === slug) {
      this.elegir_categoria_alojamiento = "todos";
    }
    else {
      this.elegir_categoria_alojamiento = slug;
    }
  }

  carrusel: string[] = ["Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10","Activa tu mejor precio ahora: usa el código AHORRA10"]




}
