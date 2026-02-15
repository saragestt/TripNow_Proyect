import { Injectable } from '@angular/core';
import {environment} from "../../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";




@Injectable({
  providedIn: 'root',
})
export class ViajesService {

  private URL = environment.apiURL;

  constructor(
      private http: HttpClient,
      ) {
  }

  getViajes(): Observable<any> {
      return this.http.get<any>(`${this.URL}/todos-viajes/`);
  }

  getCategorias(): Observable<any>{
      return this.http.get<any>(`${this.URL}/categorias/`);
  }


}
