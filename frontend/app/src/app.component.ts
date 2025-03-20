import { Component, OnInit } from '@angular/core';
import { UsuarioService } from './usuario.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  usuarios: any[] = [];

  constructor(private usuarioService: UsuarioService) { }

  ngOnInit() {
    this.usuarioService.getUsuarios().subscribe(
      (data) => {
        this.usuarios = data;
        console.log(this.usuarios); // Exibe a lista de usuários no console
      },
      (error) => {
        console.error('Erro ao buscar usuários:', error);
      }
    );
  }
}
