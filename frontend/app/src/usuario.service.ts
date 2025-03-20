import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  private apiUrl = 'http://localhost:5000/usuarios';  // URL da sua API Flask

  constructor(private http: HttpClient) { }

  // Função para obter a lista de usuários da API
  getUsuarios(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
