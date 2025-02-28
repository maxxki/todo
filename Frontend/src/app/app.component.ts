import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true, // ✅ If using standalone
  imports: [CommonModule, FormsModule], // ✅ Fixes all errors
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  tasks: { text: string; erledigt: boolean }[] = [];

  addTask(text: string) {
    if (text.trim().length === 0) return;
    this.tasks.push({ text, erledigt: false });
  }

  deleteTask(index: number) {
    this.tasks.splice(index, 1);
  }
}

